import React, { useState, useEffect } from "react";
import axios, { AxiosHeaders } from "axios";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import { Link } from "react-router-dom";
import styles from "./style.module.css";

const LoginPage = () => {
    const [ requestResponse, setRequestResponse ] = useState({
        textMessage: '',
        alertClass : ''
    })

  const initialValues = {
    email: "",
    password: "",
  };

  const onSubmit = (values) => {
    axios.post('https://orca-app-jhg4l.ondigitalocean.app/api/auth/login', values)
    .then((response) => {

        localStorage.setItem('token', response.data.token);
        localStorage.setItem('user', JSON.stringify(response.data.user))

        setRequestResponse({
            textMessage: 'login successfull, thank you',
            alertClass: 'alert alert-success'
        })
    }, (error) => {
        setRequestResponse({
            textMessage: error.response.data.message,
            alertClass: 'alert alert-danger'
        })
    })
    .catch(error => console.log(error));
  };

  const validationSchema = Yup.object({
    email: Yup.string()
      .required("email is required")
      .email("email must be a valid email"),
    password: Yup.string()
      .required("password is required")
      .min(6, "password must be at least 6 characters"),
  });

  return (
    <div className="container">
      <div className="row">
        <div className="col-md-3"></div>
        <div className="col-md-6">
          <div className={styles.wrapper}>
            <div className={ requestResponse.alertClass }>
                { requestResponse.textMessage }
            </div>
            <h2>Login</h2>
            <hr />
            <Formik
              initialValues={initialValues}
              onSubmit={onSubmit}
              validationSchema={validationSchema}
              validateOnMount
            >
              {(formik) => {
                return (
                  <Form>
                    <div className="form-group">
                      <label htmlFor="email">Email</label>
                      <Field
                        type="text"
                        name="email"
                        id="email"
                        className={
                          formik.touched.email && formik.errors.email
                            ? "form-control is-invalid"
                            : "form-control"
                        }
                      />
                      <ErrorMessage name="email">
                        {(errorMessage) => (
                          <small className="text-danger">{errorMessage}</small>
                        )}
                      </ErrorMessage>
                    </div>

                    <div className="form-group">
                      <label htmlFor="password">Password</label>
                      <Field
                        type="password"
                        name="password"
                        id="password"
                        className={
                          formik.touched.password && formik.errors.password
                            ? "form-control is-invalid"
                            : "form-control"
                        }
                      />
                      <ErrorMessage name="password">
                        {(errorMessage) => (
                          <small className="text-danger">{errorMessage}</small>
                        )}
                      </ErrorMessage>
                    </div>

                    <input
                      type="submit"
                      value="Login"
                      className="btn btn-primary btn-block"
                      disabled={!formik.isValid}
                    />
                  </Form>
                );
              }}
            </Formik>
            <br />
            <p className="text-center">
              New User? <Link to="/register">Click Here</Link>
            </p>
          </div>
        </div>
        <div className="col-md-3"></div>
      </div>
    </div>
  );
};
export default LoginPage;
