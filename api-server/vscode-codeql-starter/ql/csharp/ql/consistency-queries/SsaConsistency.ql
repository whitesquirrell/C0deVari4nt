import csharp
import semmle.code.csharp.dataflow.internal.SsaImplCommon::Consistency

class MyRelevantDefinition extends RelevantDefinition, Ssa::Definition {
  override predicate hasLocationInfo(
    string filepath, int startline, int startcolumn, int endline, int endcolumn
  ) {
    this.getLocation().hasLocationInfo(filepath, startline, startcolumn, endline, endcolumn)
  }
}
