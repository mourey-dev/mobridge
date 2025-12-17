import { Field, FieldLabel } from "./ui/field";
import { Input } from "./ui/input";
import { useFieldContext } from "@/context/form.context";

export const InputField = ({
  className,
  type,
  ...props
}: React.ComponentProps<"input">) => {
  const field = useFieldContext<string>();
  return (
    <Input
      value={field.state.value}
      onChange={(e) => field.handleChange(e.target.value)}
      type={type}
      className={className}
      {...props}
    />
  );
};

type TextFieldProps = {
  label: string;
  id: string;
  type: string;
  placeholder?: string;
  required?: boolean;
};

export const TextField = ({
  label,
  id,
  type,
  placeholder,
  required = false,
}: TextFieldProps) => {
  const field = useFieldContext<string>();

  return (
    <Field>
      <FieldLabel htmlFor={id}>{label}</FieldLabel>
      <Input
        id={id}
        type={type}
        placeholder={placeholder}
        required={required}
        value={field.state.value}
        onChange={(e) => field.handleChange(e.target.value)}
      />
    </Field>
  );
};
