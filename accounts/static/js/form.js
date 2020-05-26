
var getCookie = (name)=>{
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

class FormStart extends React.Component {
  state = {

  }
  showSnackbar = (status) => {
    var x = document.getElementById("snackbar");
    if(status == 'ERROR')
    {
      x.innerHTML = "Some error occured..";
      x.style = "background-color: red;"
      x.className = "show";
    }
    else{
      x.innerHTML = "Success..";
      x.style = "background-color: green;"
      x.className = "show";
    }
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
  }
  handleImage = (e) => {
    this.setState({
      [e.target.name] : e.target.files[0]
    })
  }
  handleChange = (e) => {
    this.setState({
      [e.target.name] : e.target.value
    })
  }
  handleSubmit = async (e) => {
    e.preventDefault()
    console.log(this.state)
    var form_data = new FormData()
    var x;
    var inp = this.props.FieldLabels;
    for(x in inp){
      
      form_data.append(`${inp[x]}`,this.state[`${inp[x]}`])
      
      console.log(`${inp[x]}`,this.state[`${inp[x]}`])
    }
    var url = this.props.post_url;
    console.log(url)
    console.log('form_data',form_data)
    var csrftoken = getCookie('csrftoken');
    axios.post(url,form_data,{
      headers:{
        'X-CSRFToken':csrftoken,
        
      }
    })
    .then(res => {
      this.showSnackbar("SUCCESS")
      console.log("YAY SUCCESS")
    })
    .catch(err =>{
      this.showSnackbar("ERROR")
      console.log("ERROR")
    })
  }
  render() {
      
      
      var f = this.props.FieldLabels;
      var t = this.props.Types;
      var p = this.props.PlaceHolders;
      var output = [];
      for(var i=0; i< f.length ;i++)
      {
          if (t[i] == 'textarea'){
              output.push(
              <p className = "fadeIn first">
              <strong><label htmlFor="id_status">{f[i]}</label></strong>
              <textarea onChange = {this.handleChange} placeholder = {p[i]} name={f[i]} cols="40" rows="10" maxLength="140" required="" id="id_status"></textarea>
              </p>
              );
          }
          else if(t[i] == 'title')
          { 
              output.push(
              <p>
              <p className = "fadeIn first">
              <strong><label htmlFor="id_status">{f[i]}:</label></strong>
              <strong><div>{p[i]}</div></strong>
              <input name={f[i]} onChange = {this.handleChange}  placeholder = {p[i]} type = "hidden" id="id_status" value = {p[i]}></input>
              </p>
              </p>
              );
          }
          else if(t[i] == 'file'){
              output.push(
                  <p className = "fadeIn first">
              <strong><label htmlFor="id_status">{f[i]}</label></strong>
              <input name={f[i]} onChange = {this.handleImage}  placeholder = {p[i]} type = {t[i]} id="id_status" ></input>
              </p>
              );
          }
          else{
              output.push(
                  <p className = "fadeIn first">
              <strong><label htmlFor="id_status">{f[i]}</label></strong>
              <input name={f[i]} onChange = {this.handleChange}  placeholder = {p[i]} type = {t[i]} id="id_status" ></input>
              </p>
              );
              
          }
      }
      output.push(<p className = "fadeIn second"> <input type="submit" className="fadeIn third" value={this.props.submitText} /> </p>)
      return (
      <div className = "wrapper fadeInDown">
      <div id="formContent">
          
          <h2 className = "active"> INFORMATION IS THE NEW OIL </h2>

          <form method = "POST" onSubmit = {this.handleSubmit} encType="multipart/form-data">
          
              {output}
          </form>

          <br/><br/><br />
          <div id="snackbar"></div>
          

      </div>
      </div>
      );
  }
  }