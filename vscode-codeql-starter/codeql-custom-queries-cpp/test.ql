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
            and not E.isConstant()
        )
    }

    // override predicate isAdditionalTaintStep(DataFlow::Node pred, DataFlow::Node succ) {
    //     exists(FunctionCall fc |
    //       fc.getTarget().hasName("malloc") and
    //       pred.asExpr() = fc.getArgument(0) and
    //       succ.asExpr().(FunctionCall).getTarget().hasGlobalName("mempool_alloc")
    //     )
    // }

    override predicate isSink(DataFlow::Node sink) {
      exists(FunctionCall fc | fc.getTarget().hasName("memcpy") and sink.asExpr() = fc.getArgument(2))
      and not sink.asExpr().isConstant()
    //   and sink.asExpr() instanceof Operation
    //   and exists(MallocSize ms | ms.getAnOperand() = sink.asExpr())
    }
}

// from FunctionCall fc, Operation ro
// where fc.getTarget().hasName("malloc") 
// and fc.getArgument(0) instanceof Operation
// and ro = fc.getArgument(0)
// select fc, ro.getAnOperand()
// select ro

// from MallocSize ms, Expr sink, FunctionCall fc
// where fc.getTarget().hasName("memcpy")
// and sink = fc.getArgument(2)
// and not sink.isConstant()
// and sink instanceof Operation
// // and ms.getAnOperand() instanceof AddExpr
// select ms, ms.getAnOperand()


from Config cfg, DataFlow::PathNode source, DataFlow::PathNode sink, MallocSize ms
where cfg.hasFlowPath(source, sink)
// select sink, source, sink, "Taint from UDF to memcpy " + source
// and source.getNode().asExpr().getValue() = ms.getAnOperand().getValue()
select source.getNode().asExpr(), ms.getAnOperand(), source, "bruh"

// from MallocSize ms
// select ms, ms.getAnOperand()