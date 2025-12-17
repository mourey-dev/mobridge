export interface LoginInterface {
  email: string;
  password: string;
}

export interface LoginResponseInterface {
  refresh: string;
  access: string;
}
