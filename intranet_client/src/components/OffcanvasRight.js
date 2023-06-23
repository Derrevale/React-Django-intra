import React from 'react';
import { Offcanvas } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
    faHome,
    faCalendar,
    faFile,
    faBook,
    faIdBadge,
    faImages,
    faSearch
} from '@fortawesome/free-solid-svg-icons';

function OffcanvasRight({ show, handleClose }) {
  return (
    <Offcanvas show={show} onHide={handleClose} placement="end">
      <Offcanvas.Header closeButton>
        <Offcanvas.Title>Menu secondaire</Offcanvas.Title>
      </Offcanvas.Header>
      <Offcanvas.Body>
        <ul>
            <li className="sp-menu-item" className="offcanvas">
                <a href="/">
                    <FontAwesomeIcon icon={faHome} className="fa-facebook"></FontAwesomeIcon> Home
                </a>
            </li>
            <li className="sp-menu-item" className="offcanvas">
                <a href="/calendar">
                    <FontAwesomeIcon icon={faCalendar} className="fa-facebook"></FontAwesomeIcon> Calendrier
                </a>
            </li>
            <li className="sp-menu-item" className="offcanvas">
                <a href="/documents">
                    <FontAwesomeIcon icon={faFile} className="fa-facebook"></FontAwesomeIcon> Documents
                </a>
            </li>
            <li className="sp-menu-item" className="offcanvas">
                <a href="/formation">
                    <FontAwesomeIcon icon={faBook} className="fa-facebook"></FontAwesomeIcon> Formation
                </a>
            </li>
            <li className="sp-menu-item" className="offcanvas">
                <a href="/carrieres">
                    <FontAwesomeIcon icon={faIdBadge} className="fa-facebook"></FontAwesomeIcon> Carrière
                </a>
            </li>
            <li className="sp-menu-item" className="offcanvas">
                <a href="/galerie">
                    <FontAwesomeIcon icon={faImages} className="fa-facebook"></FontAwesomeIcon> Galerie
                </a>
            </li>
            <li className="sp-menu-item" className="offcanvas">
                <form className="center-align">
                    <FontAwesomeIcon icon={faSearch}></FontAwesomeIcon>
                    <input
                        className="center-align"
                        type="text"
                        placeholder="Search"
                    />
                </form>
            </li>
        </ul>
      </Offcanvas.Body>
    </Offcanvas>
  );
}

export default OffcanvasRight;
