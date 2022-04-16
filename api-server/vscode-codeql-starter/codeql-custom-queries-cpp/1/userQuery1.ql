/**
 * @name User-controlled source to dangerous sink
 * @kind path-problem
 * @id template-1
 */

import cpp
import semmle.code.cpp.dataflow.TaintTracking
import DataFlow::PathGraph

class Config extends TaintTracking::Configuration {
    Config() { this = "RecvUserInputToSink" }

    override predicate isSource(DataFlow::Node source) {
<<<<<<< HEAD
        source.asExpr().(FunctionCall).getTarget().hasGlobalName("read")
=======
        source.asExpr().(FunctionCall).getTarget().hasGlobalName("mempool_alloc")
>>>>>>> 027f8e9b4bbf5b3c0221f2c524a6e005aa42a926
    }

    override predicate isSink(DataFlow::Node sink) {
      exists(FunctionCall fc | fc.getTarget().hasName("memcpy") and sink.asExpr() = fc.getArgument(2))
    }
}

from Config cfg, DataFlow::PathNode source, DataFlow::PathNode sink 
where cfg.hasFlowPath(source, sink)
<<<<<<< HEAD
select sink, source, sink, "Taint from read to memcpy " + source
=======
select sink, source, sink, "Taint from mempool_alloc to memcpy " + source
>>>>>>> 027f8e9b4bbf5b3c0221f2c524a6e005aa42a926
