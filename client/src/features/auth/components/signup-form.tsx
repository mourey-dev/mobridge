import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/shared/components/ui/card";
import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLabel,
  FieldError,
} from "@/shared/components/ui/field";
import { Link } from "@tanstack/react-router";
import { withForm } from "@/hooks/form.hook";
import { DEFAULT_REGISTER_VALUES } from "../constants/auth.constant";

export const SignupForm = withForm({
  defaultValues: DEFAULT_REGISTER_VALUES,
  props: { error: "" },
  render: ({ form, error }) => (
    <div className="flex flex-col gap-6">
      <Card>
        <CardHeader className="text-center">
          <CardTitle className="text-xl">Create your account</CardTitle>
          <CardDescription>
            Enter your email below to create your account
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form
            onSubmit={(e) => {
              e.preventDefault();
              form.handleSubmit();
            }}
          >
            <FieldGroup>
              <form.AppField name="email">
                {(field) => (
                  <field.TextField
                    label="Email"
                    id="email"
                    type="email"
                    placeholder="example@example.com"
                    required
                  />
                )}
              </form.AppField>

              <Field>
                <Field className="grid grid-cols-2 gap-4">
                  <Field>
                    <FieldLabel htmlFor="password">Password</FieldLabel>
                    <form.AppField name="password">
                      {(field) => (
                        <field.InputField
                          id="password"
                          type="password"
                          required
                        />
                      )}
                    </form.AppField>
                  </Field>

                  <Field>
                    <FieldLabel htmlFor="confirm-password">
                      Confirm Password
                    </FieldLabel>
                    <form.AppField name="confirm_password">
                      {(field) => (
                        <field.InputField
                          id="confirm-password"
                          type="password"
                          required
                        />
                      )}
                    </form.AppField>
                  </Field>
                </Field>
                <FieldDescription>
                  Must be at least 8 characters long.
                </FieldDescription>
              </Field>

              <Field>
                <FieldError>{error}</FieldError>
                <form.AppForm>
                  <form.FormButton label="Create Account" />
                </form.AppForm>
                <FieldDescription className="text-center">
                  Already have an account? <Link to="/sign-in">Sign in</Link>
                </FieldDescription>
              </Field>
            </FieldGroup>
          </form>
        </CardContent>
      </Card>
      <FieldDescription className="px-6 text-center">
        By clicking continue, you agree to our <a href="#">Terms of Service</a>{" "}
        and <a href="#">Privacy Policy</a>.
      </FieldDescription>
    </div>
  ),
});
