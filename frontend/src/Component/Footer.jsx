import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const Footer = () => {
    return (
        <footer className="bg-dark text-light py-3 mt-auto w-100">
            <div className="container">
                <div className="row text-center align-items-center">

                    {/* College Address */}
                    <div className="col-lg-4">
                        <h6 className="fw-bold">B.M.S. College of Engineering, Bangalore</h6>
                    </div>

                    {/* Copyright Text */}
                    <div className="col-lg-4">
                        <p className="mb-0">© 2024 All Rights Reserved.</p>
                    </div>

                    {/* Developer Credits */}
                    <div className="col-lg-4">
                        <p className="mb-0">
                            Developed by <span className="text-warning fw-bold">Shana, Shifa and Saleena</span>
                        </p>
                    </div>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
