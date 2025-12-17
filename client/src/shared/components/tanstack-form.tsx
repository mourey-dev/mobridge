import { useFormContext } from "@/context/form.context";
import { Button } from "./ui/button";
import { LoaderCircle } from "lucide-react";

type FormButtonProps = {
  label: string;
};

export const FormButton = ({ label }: FormButtonProps) => {
  const form = useFormContext();

  return (
    <form.Subscribe selector={(state) => state.isSubmitting}>
      {(isSubmitting) => (
        <Button type="submit" disabled={isSubmitting}>
          {label}
          {isSubmitting ? <LoaderCircle className="animate-spin" /> : null}
        </Button>
      )}
    </form.Subscribe>
  );
};
