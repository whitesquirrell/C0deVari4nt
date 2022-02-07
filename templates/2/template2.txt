/**
 * @name Potentially unsafe use of strcat
 * @description Using 'strcat' without checking the size of the source string
 *              may result in a buffer overflow
 * @kind problem
 * @id cpp/unsafe-strcat
 * @recommendation Add explicit range checks or use strncat instead
 * @link https://codeql.github.com/codeql-query-help/cpp/cpp-unsafe-strcat/
 */

import cpp
import Buffer

predicate isEffectivelyConstAccess(VariableAccess a) {
  exists(Variable v |
    a.getTarget() = v and
    v.getInitializer().getExpr().isConstant() and
    not v.getAnAccess().isUsedAsLValue()
  )
}

class StrcatSource extends VariableAccess {
  FunctionCall strcat;

  StrcatSource() {
    strcat.getTarget().hasName("strcat") and
    this = strcat.getArgument(1)
  }

  FunctionCall getStrcatCall() { result = strcat }
}

from StrcatSource src
where
  not src.getType() instanceof ArrayType and
  not exists(BufferSizeExpr bse | bse.getArg().(VariableAccess).getTarget() = src.getTarget()) and
  not isEffectivelyConstAccess(src)
select src.getStrcatCall(), "Always check the size of the source buffer when using strcat."