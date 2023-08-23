import { Link } from "react-router-dom";
import styles from'./style.module.css';

const RegisterPage = () => {

    



    return(
        <div className="container">
            <div className="row"> 
            <div className="col-md-3"></div>
            <div className="col-md-6">
                <div className={styles.wrapper}>
                    <h2>Register</h2>
                    <hr/>
                    <form>
                        <div className="form-group">
                            <label htmlFor="firstname">First Name</label>
                            <input type="text" name="firstname"
                            values={formik.values.firstname}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur} id="firstname"
                            className="form-control"/>
                            {formik.errors.firstname && formik.touched.firstname ? (<small className="text-danger">
                                {formik.errors.firstname}
                            </small>):null}
                        </div>

                        <div className="form-group">
                            <label htmlFor="firstname">Email</label>
                            <input type="email" name="email" id="email"
                            className="form-control"/>
                            values={formik.values.firstname}
                            onChange={formik.handleChange}

                        </div>
                    </form>
                </div>

            </div>

            </div>

        </div>
    )
}