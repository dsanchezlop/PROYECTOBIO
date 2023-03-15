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



}
