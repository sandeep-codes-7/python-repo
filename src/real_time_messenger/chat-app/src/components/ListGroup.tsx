import { Fragment } from "react";
function ListGroup() {
  const items = ["sandeep", "kumar", "karem"];
  return (
    <Fragment>
      <h1>list:</h1>
      <ul className="list-group">
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </Fragment>
  );
}

export default ListGroup;
