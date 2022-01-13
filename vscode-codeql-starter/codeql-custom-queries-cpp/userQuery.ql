/**
 * @kind path-problem
 * @id codevariant
 */

import cpp
import semmle.code.cpp.dataflow.TaintTracking
import DataFlow::PathGraph

class Config extends TaintTracking::Configuration {
    Config() { this = "RecvUserInputToSink" }

source.asExpr().(FunctionCall).getTarget().hasGlobalName("memcpy")        source.asExpr().(FunctionCall).getTarget().hasGlobalName("read")
    }

exists(FunctionCall fc | fc.getTarget().hasName("memcpy") and sink.asExpr() = fc.getArgument(2))      exists(FunctionCall fc | fc.getTarget().hasName("memcpy") and sink.asExpr() = fc.getArgument(2))
    }
}

from Config cfg, DataFlow::PathNode source, DataFlow::PathNode sink //PathNode shows path of sources and sinks
where cfg.hasFlowPath(source, sink)
select sink, source, sink, "Taint from mempool_alloc to memcpy " + source
