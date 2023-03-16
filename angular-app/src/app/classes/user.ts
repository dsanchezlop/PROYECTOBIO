export class User {
    #username: string;
    #name: string;
    #surname: string;
    #password: string;
    #email: string;
    #role : number;

    constructor(username: string, name: string, surname: string, password: string, email: string, role: number){
        this.#username = username;
        this.#name = name;
        this.#surname = surname;
        this.#password = password;
        this.#email = email;
        this.#role = role;
    }

    public get username() {
        return this.#username;
    }

    public get name() {
        return this.#name;
    }

    public get surname() {
        return this.#surname;
    }

    public get password() {
        return this.#password;
    }

    public get email() {
        return this.#email;
    }

    public get role() {
        return this.#role;
    }

    public set username(username){
        this.#username = username;
    }

    public set name(name){
        this.#name = name;
    }

    public set surname(surname){
        this.#surname = surname;
    }

    public set password(password){
        this.#password = password;
    }

    public set email(email){
        this.#email = email;
    }

    public set role(role){
        this.#role = role;
    }
}
