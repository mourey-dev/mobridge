import { customAxios } from "@/shared/lib/axios";
import type {
  LoginInterface,
  LoginResponseInterface,
  RegisterInterface,
  RegisterResponseInterface,
} from "../interface/auth.interface";

export const loginWithEmailAndPasswordApi = async (
  data: LoginInterface
): Promise<LoginResponseInterface> => {
  const response = await customAxios.post("/account/login/", data);
  return response.data;
};

export const registerApi = async (
  data: RegisterInterface
): Promise<RegisterResponseInterface> => {
  const response = await customAxios.post("/account/register/", data);
  return response.data;
};
