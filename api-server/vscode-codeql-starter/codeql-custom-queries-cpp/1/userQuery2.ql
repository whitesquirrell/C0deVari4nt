/**
 * @name Any source to dangerous sink
 * @kind path-problem
 * @id template-2
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
      exists(FunctionCall fc | fc.getTarget().hasName("memcpy") and sink.asExpr() = fc.getArgument(2))
      and not sink.asExpr().isConstant()
    }
}

from Config cfg, DataFlow::PathNode source, DataFlow::PathNode sink 
where cfg.hasFlowPath(source, sink)
select sink, source, sink, "Taint from all source expressions to memcpy " + source
