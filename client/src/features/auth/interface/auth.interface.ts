export interface LoginInterface {
  email: string;
  password: string;
}

export interface LoginResponseInterface {
  refresh: string;
  access: string;
}

export interface RegisterInterface {
  email: string;
  password: string;
  confirm_password: string;
}

export interface RegisterResponseInterface {
  message: string;
}
