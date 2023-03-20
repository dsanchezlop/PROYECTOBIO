import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { MyProfileComponent } from './my-profile/my-profile.component';
import { MapsComponent } from './maps/maps.component';
import { FaunaMapsComponent } from './fauna-maps/fauna-maps.component';
import { LogoutComponent } from './logout/logout.component';
import { DatabaseComponent } from './database/database.component';


const routes: Routes = [
  {
		path: '',
		redirectTo: '/home',
		pathMatch: 'full',
	},
	{
		path: 'home',
		component: HomeComponent
	},
	{
		path: 'login',
		component: LoginComponent
	},
	{
		path: 'register',
		component: RegisterComponent
	},
  	{
		path: 'profile',
		component: MyProfileComponent
	},
  	{
		path: 'maps',
		component: MapsComponent
	},
	{
		path: 'logout',
		component: LogoutComponent
	},
	{
		path: 'database',
		component: DatabaseComponent
	}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
