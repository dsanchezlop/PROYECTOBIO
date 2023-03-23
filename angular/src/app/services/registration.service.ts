import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RegistrationService {
  private apiUrl = 'http://localhost:5000/register';

  constructor(private http: HttpClient) { }

  register(username: string, password: string, name: string, surname: string, email: string, role: number) {
    const user = {
      username: username,
      password: password,
      name: name,
      surname: surname,
      email: email,
      role: 2
    };
    return this.http.post<any>(this.apiUrl, user);
  }
}
