//Ref: https://stackoverflow.com/questions/43784554/how-to-add-input-data-to-list-in-react-js

class Todo extends React.Component {
    
    constructor(props) {
      super(props);
      this.state={todos:[]};
    }
    
    save() {
      var todos = [...this.state.todos];
      todos.push(this.newText.value);
      this.setState({todos});
    }

    render(){
        return(
            <div className="list">
              <h3> Hiking Checklist</h3>
              <input type="text" ref={(ip) => {this.newText = ip}}/>
              <button onClick={this.save.bind(this)}>Save
              </button>          
              <ul>
                {this.state.todos.map(function(todo) {
                      return <li>{todo}</li>
                 })}
                
              </ul>
            </div>
        )
    }
};
ReactDOM.render(<Todo />, document.querySelector("#root"));