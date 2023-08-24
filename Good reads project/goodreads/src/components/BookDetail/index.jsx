const BookDetail = (props) => {
    const {title, description , image , author} = props.data;
    return (
        <div className="container">
            <div className="row">
                <div className="col-md-4 text-center">
                    <div className="wrapper">
                        <img src={image} alt="" className="img-fluid" />
                    </div>
                </div>

                <div className="col-md-8">
                    <div className="wrapper">
                        <h1>{title}</h1>
                        <h2>{author}</h2>
                        <p>{description}</p>
                    </div>
                </div>
            </div>

        </div>
    )

    
}

export default BookDetail;