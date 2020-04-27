class FormStart extends React.Component {
  render() {
      output = []
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
              <textarea placeholder = {p[i]} name={f[i]} cols="40" rows="10" maxlength="140" required="" id="id_status"></textarea>
              </p>
              );
          }
          else{
              output.push(
                  <p className = "fadeIn first">
              <strong><label for="id_status">{f[i]}</label></strong>
              <input name={f[i]} placeholder = {p[i]} type = {t[i]} id="id_status"></input>
              </p>
              );
              
          }
      }
      output.push(<p className = "fadeIn second"> <input type="submit" class="fadeIn third" value={this.props.submitText} /> </p>)
      return (
      <div className = "wrapper fadeInDown">
      <div id="formContent">
          
          <h2 className = "active"> INFORMATION IS THE NEW OIL </h2>

          <form method = "POST" action = {this.props.post_url}>
              {output}
          </form>

          

      </div>
      </div>
      );
  }
  }