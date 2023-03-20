import { Component, ViewChild, TemplateRef } from '@angular/core';


@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
  template: `
  <nav>
  <ul>
      <li><a href="home">Home</a></li>
      <li><a href="maps">Maps</a></li>
      <li><a href="fauna_maps">Fauna Maps</a></li>
      <li><a href="database">Database</a></li>
      <li><a href="login">Login</a></li>
      <li><a href="register">Register</a></li>
      <li><a href="profile">My Profile</a></li>
      <li><a href="logout">Logout</a></li>
  </ul>
</nav>
`
})
export class NavbarComponent {
  @ViewChild('navbarTemplate', { static: true })
  navbarTemplate!: TemplateRef<any> | null;


}
