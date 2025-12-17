import { createFormHook } from "@tanstack/react-form";

import { TextField, InputField } from "@/shared/components/tanstack-field";
import { fieldContext, formContext } from "@/context/form.context";
import { FormButton } from "@/shared/components/tanstack-form";

export const { useAppForm, withForm, withFieldGroup } = createFormHook({
  fieldComponents: {
    TextField,
    InputField,
  },
  formComponents: { FormButton },
  fieldContext,
  formContext,
});
