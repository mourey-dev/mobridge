import { useState } from "react";

export const useToggle = () => {
  const [isToggled, setIsToggled] = useState(false);

  const toggle = () => setIsToggled((prev) => !prev);

  return { isToggled, toggle };
};
