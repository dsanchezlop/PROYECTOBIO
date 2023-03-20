import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';

import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { MyProfileComponent } from './my-profile/my-profile.component';
import { MapsComponent } from './maps/maps.component';
import { HomeComponent } from './home/home.component';
import { DatabaseComponent } from './database/database.component';
import { FaunaMapsComponent } from './fauna-maps/fauna-maps.component';
import { NavbarComponent } from './navbar/navbar.component';
import { LogoutComponent } from './logout/logout.component';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    MyProfileComponent,
    MapsComponent,
    HomeComponent,
    DatabaseComponent,
    FaunaMapsComponent,
    NavbarComponent,
    LogoutComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    CommonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
