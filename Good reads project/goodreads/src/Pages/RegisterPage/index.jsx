import { Link } from "react-router-dom";
import styles from "./style.module.css";
import { useFormik } from "formik";
import * as Yup from "yup";
import axios from "axios";
import React , {useState} from 'react';

const RegisterPage = () => {

    const[requestResponse , setRequestResponse] = useState({
        textMessage: '',
        alertClass: ''
    })

  const initialValues = {
    firstname: "",
    email: "",
    password: "",
    mobile: "",
  };

  const onSubmit = (values) => {
    // console.log(values);
    axios
      .post(
        "https://orca-app-jhg4l.ondigitalocean.app/api/auth/register",
        values
      )
      .then((response) => {
        // console.log(response.data);
        setRequestResponse({
            textMessage : response.data.message,
            alertClass: 'alert alert-success'
        })
      }, (error) => {
        console.log(error);
        
      })
      .catch(error => console.log(error));
  };

  const ValidationSchema = Yup.object({
    firstname: Yup.string().required("first name is reaquired"),
    email: Yup.string()
      .required("email name is reaquired")
      .email("email should be a valid email"),
    password: Yup.string().required("password name is reaquired"),
    mobile: Yup.string()
      .required("mobile name is reaquired")
      .min(6, "password must be 6 characters long"),
  });

  const formik = useFormik({
    initialValues,
    onSubmit,
    ValidationSchema,
    validateOnChange: true,
  });

  return (
    <div className="container">
      <div className="row">
        <div className="col-md-3"></div>
        <div className="col-md-6">
          <div className={styles.wrapper}>
            <h2>Register</h2>
            <hr />
            <form onSubmit={formik.handleBlur}>
              <div className="form-group">
                <label htmlFor="firstname">First Name</label>
                <input
                  type="text"
                  name="firstname"
                  values={formik.values.firstname}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  id="firstname"
                  className={
                    formik.touched.firstname && formik.errors.firstname
                      ? "form-control is-invalid"
                      : "form-control"
                  }
                />
                {formik.errors.firstname && formik.touched.firstname ? (
                  <small className="text-danger">
                    {formik.errors.firstname}
                  </small>
                ) : null}
              </div>

              <div className="form-group">
                <label htmlFor="email">Email </label>
                <input
                  type="text"
                  name="email"
                  values={formik.values.email}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  onBlur={formik.handleBlur}
                  id="email"
                  className={
                    formik.touched.email && formik.errors.email
                      ? "form-control is-invalid"
                      : "form-control"
                  }
                />
                {formik.errors.email && formik.touched.email ? (
                  <small className="text-danger">{formik.errors.email}</small>
                ) : null}
              </div>

              <div className="form-group">
                <label htmlFor="password">Password </label>
                <input
                  type="text"
                  name="email"
                  values={formik.values.password}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  onBlur={formik.handleBlur}
                  id="password"
                  className={
                    formik.touched.password && formik.errors.password
                      ? "form-control is-invalid"
                      : "form-control"
                  }
                />
                {formik.errors.password && formik.touched.password ? (
                  <small className="text-danger">
                    {formik.errors.password}
                  </small>
                ) : null}
              </div>

              <div className="form-group">
                <label htmlFor="mobile">Mobile </label>
                <input
                  type="text"
                  name="mobile"
                  values={formik.values.mobile}
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  onBlur={formik.handleBlur}
                  id="mobile"
                  className={
                    formik.touched.Mobile && formik.errors.Mobile
                      ? "form-control is-invalid"
                      : "form-control"
                  }
                />
                {formik.errors.mobile && formik.touched.mobile ? (
                  <small className="text-danger">{formik.errors.mobile}</small>
                ) : null}
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};
export default RegisterPage;
