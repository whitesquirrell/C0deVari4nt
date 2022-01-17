/**
 * @name Any source to dangerous sink
 * @kind path-problem
 * @id template-1
 */

import cpp
import semmle.code.cpp.dataflow.TaintTracking
import DataFlow::PathGraph

class Config extends TaintTracking::Configuration {
    Config() { this = "RecvUserInputToSink" }

    override predicate isSource(DataFlow::Node source) {
        exists(Expr E |
            source.asExpr() = E
        )
    }

    override predicate isSink(DataFlow::Node sink) {
<<<<<<< HEAD
      exists(FunctionCall fc | fc.getTarget().hasName("strcpy") and sink.asExpr() = fc.getArgument(1))
=======
      exists(FunctionCall fc | fc.getTarget().hasName("memcpy") and sink.asExpr() = fc.getArgument(2))
      and not sink.asExpr().isConstant()
>>>>>>> a8786e0c2ea5da0a04877ef8076ffecf974e236d
    }
}

from Config cfg, DataFlow::PathNode source, DataFlow::PathNode sink //PathNode shows path of sources and sinks
where cfg.hasFlowPath(source, sink)
select sink, source, sink, "Taint from UDF to strcpy " + source
