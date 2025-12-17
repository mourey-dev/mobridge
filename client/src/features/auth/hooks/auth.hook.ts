import { loginWithEmailAndPasswordApi } from "../api/auth.api";
import { useMutation } from "@tanstack/react-query";

export const useLogin = () => {
  return useMutation({
    mutationFn: loginWithEmailAndPasswordApi,
    onSuccess: (data) => {
      alert(`Access Token: ${data.access}`);
    },
  });
};
