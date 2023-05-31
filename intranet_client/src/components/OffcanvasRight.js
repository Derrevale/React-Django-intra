import React from 'react';
import { Offcanvas } from 'react-bootstrap';

function OffcanvasRight({ show, handleClose }) {
  return (
    <Offcanvas show={show} onHide={handleClose} placement="end">
      <Offcanvas.Header closeButton>
        <Offcanvas.Title>Offcanvas Right</Offcanvas.Title>
      </Offcanvas.Header>
      <Offcanvas.Body>
        Content for your offcanvas goes here
      </Offcanvas.Body>
    </Offcanvas>
  );
}

export default OffcanvasRight;
