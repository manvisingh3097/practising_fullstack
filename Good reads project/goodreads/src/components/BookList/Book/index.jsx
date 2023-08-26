const Book = (props) => {
  const { title, image } = props.data;

  return(
      <div className="col-sm-3">
          <div className="card">
              <img src={ image } alt="" className="card-image-top" />
              <div className="card-body">
                  <div className="card-title">
                      { title }
                  </div>
                  <a href="#" className="btn btn-dark btn-block">Show Details</a>
              </div>
          </div>
      </div>
  )
}
export default Book;