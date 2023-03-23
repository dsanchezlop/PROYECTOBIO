import { Component, ViewChild, TemplateRef } from '@angular/core';


@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
  template: `
  <nav>
  <ul>
      <li><a routerLink="/">Home</a></li>
      <li><a routerLink="/maps">Maps</a></li>
      <li><a routerLink="/fauna_maps">Fauna Maps</a></li>
      <li><a routerLink="/database">Database</a></li>
      <li><a routerLink="/login">Login</a></li>
      <li><a routerLink="/register">Register</a></li>
      <li><a routerLink="/profile">My Profile</a></li>
      <li><a routerLink="/logout">Logout</a></li>
  </ul>
</nav>
`
})
export class NavbarComponent {
  @ViewChild('navbarTemplate', { static: true })
  navbarTemplate!: TemplateRef<any> | null;


}
