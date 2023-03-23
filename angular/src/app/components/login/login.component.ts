import { Component } from '@angular/core';
import { LoginService } from '../../services/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html'
})
export class LoginComponent {
  constructor(private loginService: LoginService) { }

  login(username: string, password: string) {
    this.loginService.login(username, password).subscribe(response => {
      console.log(response);
    }, error => {
      console.error(error);
    });
  }
}
