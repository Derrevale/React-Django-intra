import '../styles/Navbar.css'
import '../styles/bootstrap.min.css'
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faHome, faCalendar, faFile, faBook, faIdBadge, faImages, faSearch} from "@fortawesome/free-solid-svg-icons";
import {faFacebook, faYoutube, faLinkedin} from "@fortawesome/free-brands-svg-icons";

function Navbar() {
    return <header id="banner_header">
        <div className="container">
            <div className="container-inner">
                <div className="row">
                    <div className="header_logo col-auto">
                        <div className="header_column">
                            <div className="logo">
                                <a href="/">
                                    <img className="logo-image  ls-is-cached lazyloaded"
                                         data-srcset="https://intra.silva-medical.be/images/silva-intranet.png 1x"
                                         data-src="https://intra.silva-medical.be/images/silva-intranet.png"
                                         alt="Intranet"
                                         data-size="auto"
                                         srcSet="https://intra.silva-medical.be/images/silva-intranet.png 1x"
                                         src="ArticleList"></img>
                                </a>
                            </div>
                        </div>
                    </div>


                    <div className="header_menu col flex-auto">
                        <div className="sp-column d-flex justify-content-end align-items-center">
                            <nav className="sp-megamenu-wrapper d-flex" role="navigation">
                                <ul className="sp-megamenu-parent menu-animation-fade-up d-none d-lg-block">
                                    <li className="sp-menu-item">
                                        <a href="/">
                                            <FontAwesomeIcon icon={faHome} className="fa-facebook"></FontAwesomeIcon> Home
                                        </a>
                                    </li>
                                    <li className="sp-menu-item">
                                        <a href="/events">
                                            <FontAwesomeIcon icon={faCalendar} className="fa-facebook"></FontAwesomeIcon> Garde
                                        </a>
                                    </li>
                                    <li className="sp-menu-item">
                                        <a href="/Documents">
                                            <FontAwesomeIcon icon={faFile} className="fa-facebook"></FontAwesomeIcon> Documents
                                        </a>
                                    </li>
                                    <li className="sp-menu-item">
                                        <a href="https://silvamedic.lms.sapsf.eu/learning/user/personal/viewPersonalHome.do?OWASP_CSRFTOKEN=TYES-8K4D-BBIC-1OAO-AXS6-DT40-ERNO-8HXI&fromSF=Y&fromDeepLink=true">
                                            <FontAwesomeIcon icon={faBook} className="fa-facebook"></FontAwesomeIcon> Formation
                                        </a>
                                    </li>
                                    <li className="sp-menu-item">
                                        <a href="https://hcm55.sapsf.eu/sf/careers/jobsearch?bplte_company=silvamedic">
                                            <FontAwesomeIcon icon={faIdBadge} className="fa-facebook"></FontAwesomeIcon> Carrière
                                        </a>
                                    </li>
                                    <li className="sp-menu-item">
                                        <a href="/Galerie">
                                            <FontAwesomeIcon icon={faImages} className="fa-facebook"></FontAwesomeIcon> Galerie
                                        </a>
                                    </li>
                                    <li className="sp-menu-item">
                                        <a href="/off-menu">
                                            <span className="..."></span> Off-menu
                                        </a>
                                    </li>
                                </ul>
                            </nav>

                        </div>
                    </div>


                </div>
            </div>
        </div>
    </header>

}

export default Navbar