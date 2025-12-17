import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";
import { AxiosError } from "axios";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export const getErrorMessage = (error: unknown): string => {
  if (!(error instanceof AxiosError)) {
    return "An unknown error occurred";
  }

  if (!error.response) {
    return "Network error. Please check your internet connection.";
  }

  // 1. Capture the raw data
  const data = error.response.data;

  // 2. Scenario: Backend returns a simple string (e.g., "User not found")
  if (typeof data === "string") {
    // If it's a short message, return it. If it's a giant HTML page (like an Nginx 404), fallback.
    return data.length < 100 ? data : "Server error";
  }

  // 3. Scenario: Backend returns an object (JSON)
  if (data && typeof data === "object" && !Array.isArray(data)) {
    // Cast as a Record so we can access keys safely
    const errorObj = data as Record<string, unknown>;

    // Check keys one by one. We must cast the value to string to be safe.
    const message = errorObj.detail || errorObj.message || errorObj.error;

    if (typeof message === "string") {
      return message;
    }

    // Handle Validation Arrays
    // Check if 'errors' exists and is an array
    if (Array.isArray(errorObj.errors)) {
      const firstError = errorObj.errors[0];
      if (typeof firstError === "string") {
        return firstError;
      }
    }
  }

  // 4. Fallback: If we couldn't find a readable message
  return `Request failed with status ${error.response.status}`;
};
