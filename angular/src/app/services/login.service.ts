import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<any> {
    const user = { username, password };
    return this.http.post<any>('api/login', user);
  }
}
