import { Body, Controller, Post } from '@nestjs/common';
import { AuthService } from '../services/auth.service';

@Controller('auth')
export class AuthController {
  constructor(private readonly authService: AuthService) {}

  @Post('login')
  login(@Body() body: { stdNum: string; password: string }) {
    return this.authService.login(body.stdNum, body.password);
  }
}
