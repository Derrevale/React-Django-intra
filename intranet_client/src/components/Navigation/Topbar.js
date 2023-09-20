import React, { useContext } from 'react';
import '../../styles/Topbar.css';
import '../../styles/bootstrap.min.css';
import { LanguageContext } from '../../services/LanguageContext'; // Ajustez le chemin selon votre structure de dossier
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEnvelope, faLanguage } from "@fortawesome/free-solid-svg-icons";
import { faFacebook, faYoutube, faLinkedin } from "@fortawesome/free-brands-svg-icons";

function Topbar() {
    const { setLanguage } = useContext(LanguageContext);

    return (
        <div id="sp-top-bar">
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
                                            <FontAwesomeIcon icon={faYoutube} className="fa fa-youtube"></FontAwesomeIcon>
                                        </a>
                                    </li>
                                    <li className="">
                                        <a target="_blank" rel="noopener noreferrer"
                                            href="https://be.linkedin.com/company/silva-medical"
                                            aria-label="Linkedin">
                                            <FontAwesomeIcon icon={faLinkedin} className="fa fa-linkedin"></FontAwesomeIcon>
                                        </a>
                                    </li>
                                    <li className="">
                                        <button onClick={() => setLanguage('fr')} aria-label="Français">
                                            <FontAwesomeIcon icon={faLanguage} className="fa fa-language"></FontAwesomeIcon> FR
                                        </button>
                                    </li>
                                    <li className="">
                                        <button onClick={() => setLanguage('nl')} aria-label="Nederlands">
                                            <FontAwesomeIcon icon={faLanguage} className="fa fa-language"></FontAwesomeIcon> NL
                                        </button>
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
    );
}

export default Topbar;
