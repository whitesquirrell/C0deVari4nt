import javascript

// Select all expressions whose string value contains the word "two"
predicate containsTwo(DataFlow::Node node) {
  node.getStringValue().matches("%two%")
  or
  containsTwo(node.getAPredecessor())
  or
  containsTwo(node.(StringOps::Concatenation).getAnOperand())
}

from Expr e
where containsTwo(e.flow())
select e
