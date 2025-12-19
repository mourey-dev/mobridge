import { loginWithEmailAndPasswordApi, registerApi } from "../api/auth.api";
import { useMutation } from "@tanstack/react-query";

export const useLogin = () => {
  return useMutation({
    mutationFn: loginWithEmailAndPasswordApi,
    onSuccess: (data) => {
      alert(`Access Token: ${data.access}`);
    },
  });
};

export const useRegister = () => {
  return useMutation({
    mutationFn: registerApi,
    onSuccess: (data) => {
      alert(data.message);
    },
  });
};
