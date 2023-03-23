import { Component } from '@angular/core';
import { RegistrationService } from '../../services/registration.service';

@Component({
  selector: 'app-registration',
  templateUrl: './register.component.html'
})
export class RegisterComponent {
  constructor(private registrationService: RegistrationService) { }

  register(username: string, password: string, name: string, surname: string, email: string, role: number) {
    this.registrationService.register(username, password, name, surname, email, role).subscribe(response => {
      console.log(response);
    }, error => {
      console.error(error);
    });
  }
}
