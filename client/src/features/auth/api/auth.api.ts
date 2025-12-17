import { customAxios } from "@/shared/lib/axios";
import type {
  LoginInterface,
  LoginResponseInterface,
} from "../interface/auth.interface";

export const loginWithEmailAndPasswordApi = async (
  data: LoginInterface
): Promise<LoginResponseInterface> => {
  const response = await customAxios.post("/account/login/", data);
  return response.data;
};
