/**
 * @kind path-problem
 */

import semmle.code.cpp.dataflow.TaintTracking
import semmle.code.cpp.valuenumbering.GlobalValueNumbering
import DataFlow::PathGraph

class Conf extends TaintTracking::Configuration {
  Conf() { this = "Conf" }

  override predicate isSource(DataFlow::Node source) {
    source.asDefiningArgument() =
      any(Call call | call.getTarget().hasName("recvfrom")).getArgument(1)
  }

  override predicate isSink(DataFlow::Node sink) {
    sink.asExpr() = any(Call call | call.getTarget().hasName("memcpy")).getArgument(2)
  }

  override predicate isAdditionalTaintStep(DataFlow::Node node1, DataFlow::Node node2) {
    globalValueNumber(node1.asDefiningArgument()).getAnExpr() = node2.asExpr()
  }
}

from Conf conf, DataFlow::PathNode source, DataFlow::PathNode sink
where conf.hasFlowPath(source, sink)
select sink.getNode(), source, sink, "Taint from recvfrom to memcpy with additional taint step to transfer taint between pointers"
