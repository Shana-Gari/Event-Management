import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark shadow-sm p-3">
            <div className="container">
                <div className="row w-100 text-center align-items-center">

                    {/* College Name (Left Section) */}
                    <div className="col-lg-4 text-start">
                        <a className="navbar-brand fw-bold fs-4" href="/">
                            B.M.S. College of Engineering
                        </a>
                    </div>

                    {/* Department Name (Center Section) */}
                    <div className="col-lg-4 text-center">
                        <span className="text-warning fw-bold fs-5">Department of M.C.A.</span>
                    </div>

                    {/* Login & Signup Buttons (Right Section) */}
                    <div className="col-lg-4 text-end">
                        <a href="/login" className="btn btn-outline-light me-2">Login</a>
                        <a href="/signup" className="btn btn-warning">Signup</a>
                    </div>

                </div>
            </div>
        </nav>
    );
};

export default Navbar;
