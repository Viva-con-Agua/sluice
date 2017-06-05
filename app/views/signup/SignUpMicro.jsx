import $ from 'jquery'
import React, { Component } from 'react';



export default class SignUpMicro extends React.Component {
	
	constructor(props) {
		super(props);

		this.state = {
			name: '',
			link:'',
			version: '',
			doku: ''
		};
		this.handleNameChange = this.handleNameChange.bind(this);
		this.handleUrlChange = this.handleUrlChange.bind(this);
		this.handleVersionChange = this.handleVersionChange.bind(this)
		this.handleSubmit = this.handleSubmit.bind(this);
	}

	handleNameChange(event) {
		this.setState({name: event.target.value});
	}
	handleUrlChange(event) {
		this.setState({url: event.target.value});
	}
	handleVersionChange(event) {
		this.setState({version: event.target.value});
	}

	handleSubmit(event) {
	
		event.preventDefault();	
	}

	render() {
		return(
			<div className='signupMicro'>
				Add Microservice
				<form>
  				<label>
    				Microservice:
    				<input 
							type="text" 
							name="MicroserviceNameInput"
							onChange={this.handleNameChange}
							/>
  				</label>
  					<label>
    				Url:
    				<input 
							type="text" 
							name="MicroserviceUrlInput"
							onChange={this.handleUrlChange}
							/>
  				</label>
					<label>
    				Version:
    				<input 
							type="text" 
							name="MicroserviceVersionInput" 
							onChange={this.handleVersionChange}
							/>
  				</label>
				<input type="submit" value="Submit" />
				</form>
      </div>
		);
	}
}
