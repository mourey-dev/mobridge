import { GalleryVerticalEnd } from "lucide-react";

import { LoginForm } from "../components/login-form";
import { useAppForm } from "@/hooks/form.hook";
import { DEFAULT_LOGIN_VALUES } from "../constants/auth.constant";
import { useLogin } from "../hooks/auth.hook";
import { getErrorMessage } from "@/shared/lib/utils";

export const LoginPage = () => {
  const { mutateAsync, error, isError } = useLogin();
  const form = useAppForm({
    defaultValues: DEFAULT_LOGIN_VALUES,
    onSubmit: async ({ value }) => await mutateAsync(value),
  });

  return (
    <div className="bg-muted flex min-h-svh flex-col items-center justify-center gap-6 p-6 md:p-10">
      <div className="flex w-full max-w-sm flex-col gap-6">
        <a href="#" className="flex items-center gap-2 self-center font-medium">
          <div className="bg-primary text-primary-foreground flex size-6 items-center justify-center rounded-md">
            <GalleryVerticalEnd className="size-4" />
          </div>
          Acme Inc.
        </a>
        <LoginForm form={form} error={isError ? getErrorMessage(error) : ""} />
      </div>
    </div>
  );
};
