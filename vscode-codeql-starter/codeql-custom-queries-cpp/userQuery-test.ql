/**
 * @name Any source to dangerous sink
 * @kind path-problem
 * @id template-2
 */

import cpp
import semmle.code.cpp.dataflow.TaintTracking
import DataFlow::PathGraph


class MallocSize extends AddExpr {
    MallocSize () {
        exists(
            FunctionCall fc | 
            fc.getTarget().hasName("malloc") and 
            fc.getArgument(0) instanceof AddExpr and
            this = fc.getArgument(0)
          )
    }

    predicate isVariableWithin(Operation var){
        this.getAnOperand() = var
    }
}

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
    //   and sink.asExpr() instanceof Operation
    //   and exists(MallocSize ms | ms.isVariableWithin(sink.asExpr()))
    }
}

from Config cfg, DataFlow::PathNode source, DataFlow::PathNode sink //PathNode shows path of sources and sinks
where cfg.hasFlowPath(source, sink)
select sink, source, sink, "Taint from UDF to memcpy " + source
