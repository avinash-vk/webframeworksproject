
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
  render() {
    
      var csrftoken = getCookie('csrftoken');
      
      var f = this.props.FieldLabels;
      var t = this.props.Types;
      var p = this.props.PlaceHolders;
      var output = [];
      for(var i=0; i< f.length ;i++)
      {
          if (t[i] == 'textarea'){
              output.push(
              <p className = "fadeIn first">
              <strong><label for="id_status">{f[i]}</label></strong>
              <textarea placeholder = {p[i]} name={f[i]} cols="40" rows="10" maxLength="140" required="" id="id_status"></textarea>
              </p>
              );
          }
          else if(t[i] == 'title')
          { 
              output.push(
              <p>
              <p className = "fadeIn first">
              <strong><label for="id_status">{f[i]}:</label></strong>
              <strong><div>{p[i]}</div></strong>
              <input name={f[i]} placeholder = {p[i]} type = "hidden" id="id_status" value = {p[i]}></input>
              </p>
              </p>
              );
          }
          else if(t[i] == 'select'){
              output.push(
                <p className = "fadeIn first">
                <strong><label for="id_status">Status:</label></strong>
                <select name="status" id="id_status">
                <option value="0" selected="">Draft</option>
              
                <option value="1">Publish</option>
              
              </select>
              </p>
              )
          }
          else{
              output.push(
                  <p className = "fadeIn first">
              <strong><label for="id_status">{f[i]}</label></strong>
              <input name={f[i]} placeholder = {p[i]} type = {t[i]} id="id_status" ></input>
              </p>
              );
              
          }
      }
      output.push(<p className = "fadeIn second"> <input type="submit" className="fadeIn third" value={this.props.submitText} /> </p>)
      return (
      <div className = "wrapper fadeInDown">
      <div id="formContent">
          
          <h2 className = "active"> INFORMATION IS THE NEW OIL </h2>

          <form method = "POST" action = {this.props.post_url} enctype="multipart/form-data">
          <   input type="hidden" name="csrfmiddlewaretoken" value={csrftoken} />
              {output}
          </form>

          

      </div>
      </div>
      );
  }
  }