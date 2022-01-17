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
      exists(FunctionCall fc | fc.getTarget().hasName("strcpy") and sink.asExpr() = fc.getArgument(1))
    }
}

from Config cfg, DataFlow::PathNode source, DataFlow::PathNode sink //PathNode shows path of sources and sinks
where cfg.hasFlowPath(source, sink)
select sink, source, sink, "Taint from UDF to strcpy " + source
