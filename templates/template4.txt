/**
 * @name All source functions to BannedStringCopyFunctions
 * @kind path-problem
 * @id template-4
 */

import cpp
import semmle.code.cpp.dataflow.TaintTracking
import DataFlow::PathGraph

class BannedStringCopyFunctions extends Function {
  BannedStringCopyFunctions() {
    exists(string name |
    hasGlobalOrStdName(name) and
    (name = "strcpy" or name = "strcpyA" or name = "strcpyW" or name = "wcscpy" or
    name = "_tcscpy" or name = "_mbscpy" or name = "StrCpy" or name = "StrCpyA" or
    name = "StrCpyW" or name = "lstrcpy" or name = "lstrcpyA" or name = "lstrcpyW" or
    name = "_tccpy" or name = "_mbccpy" or name = "_ftcscpy" or name = "strncpy" or
    name = "wcsncpy" or name = "_tcsncpy" or name = "_mbsncpy" or name = "_mbsnbcpy" or
    name = "StrCpyN" or name = "StrCpyNA" or name = "StrCpyNW" or name = "StrNCpy" or
    name = "strcpynA" or name = "StrNCpyA" or name = "StrNCpyW" or name = "lstrcpyn" or
    name = "lstrcpynA" or name = "lstrcpynW" )
    )
  }
}

class Config extends TaintTracking::Configuration {
  Config() { this = "RecvUserInputToSink" }

    override predicate isSource(DataFlow::Node source) {
      exists(FunctionCall fc | source.asExpr() = fc
      )
  }


    override predicate isSink(DataFlow::Node sink) {
        exists(FunctionCall fc, BannedStringCopyFunctions banned | fc.getTarget().getName().matches(banned.toString()) and sink.asExpr() = fc)
      }
    }


from Config cfg, DataFlow::PathNode source, DataFlow::PathNode sink //PathNode shows path of sources and sinks
where cfg.hasFlowPath(source, sink)
select sink, source, sink, "Taint from all source functions to BannedStringCopyFunctions"
