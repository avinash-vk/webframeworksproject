import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

const likecolor = 'red'; //color when liked
const unlikecolor = 'blue'; //color when not liked

const savetext=  'bg-navy fa fa-save';
const unsavetext = 'bg-orange fa fa-save';
class SaveButton extends React.Component
{
    constructor(props){
        super(props);
        if(this.props.comp in this.props.savelist)
        {
            this.state = {
                text: unsavetext
            }
        }
        else{
            this.state = {
               
                text:savetext
            }
        }
    }
    
    render(){
        clicked = () => {
            // call set save function
            if (this.state.text === unsavetext)
                this.unsave();
            else 
                this.save();
        }

        save = () => {
            this.setState({
                
                text:unsavetext
            })
        }
        unsave = () => {
            this.setState({
                
                text:savetext
            })
        }
        return(
            <a className ={"btn btn-primary "+ this.state.text} onclick = {this.clicked} />
        )
    }
}

class LikeButton extends React.Component 
{
    constructor(props){
        super(props);
        if(this.props.comp in this.props.likelist)
        {
            
            this.state = {
                color:unlikecolor,
                text:'fa fa-thumbs-up'
            }
        }
        else{
            this.state = {
                color:likecolor,
                text:'btn-danger fa fa-thumbs-down'
            }
        }
    }
    
    render(){
        clicked = () => {
            // call set like function
            if (this.state.color === 'red')
                this.unlike();
            else 
                this.like();
        }

        like = () => {
            this.setState({
                color: likecolor,
                text:"btn-danger fa fa-thumbs-down"
            })
        }
        unlike = () => {
            this.setState({
                color:unlikecolor,
                text:"fa fa-thumbs-up"
            })
        }
        return(
        <a className ={"btn btn-primary "+ this.state.text} onclick = {this.clicked} />
        )
    }
}

class BlogList extends React.Component{
    constructor(props)
        super(props)
    render(){
        let children = []
        forEach(blog in this.props.blogslist)
                children.push(<Blog blog = {blog} likelist = {this.props.likelist} savelist= {this.props.savelist} />);
    }
    output = [<div>here<div className="row"> { children } </div></div>]
    
    return ({output});
}


class Blog extends React.Component {
  
  render() {
    return (
    
      <div className="Blog"> 
        <div className ="col-lg-4 col-sm-6 mb-4">
            <div className="portfolio-item">
                
                <div className="portfolio-caption">
                    <div className="portfolio-caption-heading">{this.props.blog.title}</div>
                </div>
                <a className ="portfolio-link" data-toggle="modal" href={'#portfolio-modal-blog'+this.props.blog.id}>
                <div className ="portfolio-hover">
                    <div className ="portfolio-hover-content"><i className ="fas fa-plus fa-3x"></i></div>
                </div>
                </a>
                <div className ="portfolio-caption">
                    <p className ="card-text text-muted h6">{this.props.post.author} | {this.props.post.created_on}</p>
                    <div className ="portfolio-caption-subheading text-muted">{this.props.post.content}</div>
                </div>
            </div>
        </div>   

        <div className ="portfolio-modal modal fade" id="portfolio-modal{{ post.id }}" tabindex="-1" role="dialog" aria-hidden="true" style="margin-left: 140px;">
            <div className ="modal-dialog">
                <div className ="modal-content">
                    <div className ="close-modal" data-dismiss="modal"><i className ="fas fa-2x fa-window-close text-primary mb-4"></i></div>
                    <div className ="container" style="align-self: center;">
                        <div className ="row justify-content-center">
                            <div className ="col-lg-8">
                                <div className ="modal-body">
                                    
                                    <h2 className ="portfolio-caption-heading"> post.title }}</h2>
                                    <p> {this.props.blog.author}  |  {this.props.blog.created_on}</p>
                                    <p> {this.props.blog.content} | safe </p>
                                    <div>  
                                        <span className ="card-text text-muted h6"> {this.props.blog.likes.count } Likes
                                                <LikeButton likelist = {this.props.likelist} comp = {this.props.blog} />                                             
                                            <br/>   
                                                <SaveButton savelist = {this.props.savelist} comp = {this.props.blog} />
                                        </span>    
                                    </div>
                                    <br/>
                                    {
                                        // add comments here 
                                    }
                                    <br/>
                                    {/* //if(user.is_authenticated and user == post.author) : 
                                    
                                        <a href="{% url 'post_update' post.slug  %}" className ="btn btn-primary">Update</a>
                                        <a href="{% url 'post_delete' post.slug  %}" className ="btn btn-primary" onclick="return confirm('Are you sure you want to delete this?')">Delete</a>
                                    */ }
                                    {/*% elif follow 
                                     
                                    <div>                                      
                                            <h3>Leave a comment</h3>
                                            <form method = "post">
                                                % csrf_token %}
                                                 comment_form.as_p }}
                                                <button type="submit" className ="btn btn-primary  btn-lg">Post</button>    
                                            </form>
                                        </div>   */ 
                                    }
                                    <button className ="btn btn-primary" data-dismiss="modal" type="button"><i className ="fas fa-times mr-1"></i>Close Project</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br/>
    </div>
    
    );
  }
}
console.log("here");
const domContainer = document.getElementById('blog_display');
console.log(domContainer)
var likelist = domContainer.getAttribute('likelist');
var savelist = domContainer.getAttribute('savelist');
var blogslist = domContainer.getAttribute('blogslist');
ReactDOM.render(<div>here<BlogList blogslist = {blogslist} likelist = {likelist} savelist = {savelist} /></div>, domContainer);
