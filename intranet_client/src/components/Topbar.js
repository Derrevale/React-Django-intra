import '../styles/Topbar.css';
import '../styles/bootstrap.min.css';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faEnvelope} from "@fortawesome/free-solid-svg-icons";
import {faFacebook, faYoutube, faLinkedin} from "@fortawesome/free-brands-svg-icons";

function Topbar() {
    return <div id="sp-top-bar">
        <div className="container">
            <div className="container-inner">
                <div className="row">
                    <div className="col-lg-6">
                        <div className="sp-column text-center text-lg-start">
                            <ul className="social-icons">
                                <li className="">
                                    <a target="_blank" rel="noopener noreferrer"
                                       href="https://fr-fr.facebook.com/SILVA-medical-129395323813144/"
                                       aria-label="Facebook">
                                        <FontAwesomeIcon icon={faFacebook} className="fa fa-facebook"></FontAwesomeIcon>
                                    </a>
                                </li>
                                <li className="">
                                    <a target="_blank" rel="noopener noreferrer"
                                       href="https://www.youtube.com/channel/UCMCdKsRVd7o_PdBr39AnwCA/featured"
                                       aria-label="Youtube">
                                        <FontAwesomeIcon icon={faYoutube} className="fa fa-facebook"></FontAwesomeIcon>
                                    </a>
                                </li>
                                <li className="">
                                    <a
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        href="https://be.linkedin.com/company/silva-medical"
                                        aria-label="Linkedin">
                                        <FontAwesomeIcon icon={faLinkedin} className="fa fa-facebook"></FontAwesomeIcon>
                                    </a>
                                </li>
                            </ul>
                            <div className="sp-module">
                                <div className="sp-module-content">
                                    <div className="mod-languages"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="col-lg-6">
                        <div className="sp-column text-center text-lg-end">


                            <FontAwesomeIcon icon={faEnvelope} className=""></FontAwesomeIcon>
                            <a href="mailto:communication@silva-medical.be">
                                communication@silva-medical.be
                            </a>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

}

export default Topbar;